const rail = document.getElementById("rail");
const panels = [...document.querySelectorAll(".panel")];
const progress = document.getElementById("progress");
const dotsWrap = document.getElementById("dots");
const prevBtn = document.getElementById("prev");
const nextBtn = document.getElementById("next");
const langBtns = [...document.querySelectorAll(".lang [data-lang]")];

let index = 0;
const saved = localStorage.getItem("portfolio-lang");
let lang =
  saved === "fr" || saved === "en"
    ? saved
    : (navigator.language || "").toLowerCase().startsWith("fr")
      ? "fr"
      : "en";

panels.forEach((_, i) => {
  const b = document.createElement("button");
  b.type = "button";
  b.setAttribute("aria-label", `Page ${i + 1}`);
  b.addEventListener("click", () => go(i));
  dotsWrap.appendChild(b);
});

const dots = [...dotsWrap.querySelectorAll("button")];

function t(key) {
  const pack = window.I18N?.[lang] || window.I18N?.en || {};
  return pack[key] ?? window.I18N?.en?.[key] ?? key;
}

function applyLang() {
  document.documentElement.lang = lang;
  localStorage.setItem("portfolio-lang", lang);

  document.querySelectorAll("[data-i18n]").forEach((el) => {
    el.textContent = t(el.dataset.i18n);
  });
  document.querySelectorAll("[data-i18n-html]").forEach((el) => {
    el.innerHTML = t(el.dataset.i18nHtml);
  });
  document.querySelectorAll("[data-i18n-aria]").forEach((el) => {
    el.setAttribute("aria-label", t(el.dataset.i18nAria));
  });
  document.querySelectorAll("[data-i18n-content]").forEach((el) => {
    el.setAttribute("content", t(el.dataset.i18nContent));
  });

  langBtns.forEach((btn) => {
    const on = btn.dataset.lang === lang;
    btn.classList.toggle("on", on);
    btn.setAttribute("aria-pressed", on ? "true" : "false");
  });

  sync();
}

function go(i, smooth = true) {
  index = Math.max(0, Math.min(panels.length - 1, i));
  panels[index].scrollIntoView({
    behavior: smooth ? "smooth" : "auto",
    inline: "start",
    block: "nearest",
  });
  sync();
}

function sync() {
  panels.forEach((p, i) => p.classList.toggle("is-active", i === index));
  dots.forEach((d, i) => d.classList.toggle("on", i === index));
  const p = panels[index];
  progress.textContent =
    (lang === "en" ? p.dataset.labelEn : p.dataset.labelFr) || "";
}

function nearest() {
  const left = rail.scrollLeft;
  let best = 0;
  let dist = Infinity;
  panels.forEach((p, i) => {
    const d = Math.abs(p.offsetLeft - left);
    if (d < dist) {
      dist = d;
      best = i;
    }
  });
  return best;
}

let ticking = false;
rail.addEventListener(
  "scroll",
  () => {
    if (ticking) return;
    ticking = true;
    requestAnimationFrame(() => {
      index = nearest();
      sync();
      ticking = false;
    });
  },
  { passive: true }
);

prevBtn.addEventListener("click", () => go(index - 1));
nextBtn.addEventListener("click", () => go(index + 1));

langBtns.forEach((btn) => {
  btn.addEventListener("click", () => {
    lang = btn.dataset.lang;
    applyLang();
  });
});

document.querySelectorAll("[data-go]").forEach((el) => {
  el.addEventListener("click", (e) => {
    e.preventDefault();
    go(Number(el.dataset.go));
  });
});

window.addEventListener("keydown", (e) => {
  if (["ArrowRight", "PageDown", " "].includes(e.key)) {
    e.preventDefault();
    go(index + 1);
  } else if (["ArrowLeft", "PageUp"].includes(e.key)) {
    e.preventDefault();
    go(index - 1);
  } else if (e.key === "Home") {
    e.preventDefault();
    go(0);
  } else if (e.key === "End") {
    e.preventDefault();
    go(panels.length - 1);
  }
});

rail.addEventListener(
  "wheel",
  (e) => {
    if (Math.abs(e.deltaY) > Math.abs(e.deltaX)) {
      e.preventDefault();
      rail.scrollLeft += e.deltaY;
    }
  },
  { passive: false }
);

applyLang();
rail.focus({ preventScroll: true });
