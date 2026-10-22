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

const mobileMq = window.matchMedia("(max-width: 768px)");
function isMobile() {
  return mobileMq.matches;
}

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
    let key = el.getAttribute("data-i18n") || "";
    if (key === "cover.nudge" && isMobile()) key = "cover.nudgeMobile";
    el.textContent = t(key);
  });
  document.querySelectorAll("[data-i18n-html]").forEach((el) => {
    el.innerHTML = t(el.getAttribute("data-i18n-html") || "");
  });
  document.querySelectorAll("[data-i18n-aria]").forEach((el) => {
    el.setAttribute("aria-label", t(el.getAttribute("data-i18n-aria") || ""));
  });
  document.querySelectorAll("[data-i18n-content]").forEach((el) => {
    el.setAttribute("content", t(el.getAttribute("data-i18n-content") || ""));
  });

  langBtns.forEach((btn) => {
    const on = btn.dataset.lang === lang;
    btn.classList.toggle("on", on);
    btn.setAttribute("aria-pressed", on ? "true" : "false");
  });

  document.body.classList.toggle("is-mobile", isMobile());
  sync();
}

function go(i, smooth = true) {
  index = Math.max(0, Math.min(panels.length - 1, i));
  panels[index].scrollIntoView({
    behavior: smooth ? "smooth" : "auto",
    inline: isMobile() ? "nearest" : "start",
    block: isMobile() ? "start" : "nearest",
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
  let best = 0;
  let dist = Infinity;
  if (isMobile()) {
    const top = rail.scrollTop;
    panels.forEach((p, i) => {
      const d = Math.abs(p.offsetTop - top);
      if (d < dist) {
        dist = d;
        best = i;
      }
    });
  } else {
    const left = rail.scrollLeft;
    panels.forEach((p, i) => {
      const d = Math.abs(p.offsetLeft - left);
      if (d < dist) {
        dist = d;
        best = i;
      }
    });
  }
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
  const nextKeys = isMobile()
    ? ["ArrowDown", "ArrowRight", "PageDown", " "]
    : ["ArrowRight", "PageDown", " "];
  const prevKeys = isMobile()
    ? ["ArrowUp", "ArrowLeft", "PageUp"]
    : ["ArrowLeft", "PageUp"];
  if (nextKeys.includes(e.key)) {
    e.preventDefault();
    go(index + 1);
  } else if (prevKeys.includes(e.key)) {
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

/* Desktop only: map vertical wheel to horizontal rail */
rail.addEventListener(
  "wheel",
  (e) => {
    if (isMobile()) return;
    if (Math.abs(e.deltaY) > Math.abs(e.deltaX)) {
      e.preventDefault();
      rail.scrollLeft += e.deltaY;
    }
  },
  { passive: false }
);

/* Touch swipe helper on mobile (panel-to-panel) */
let touchY = null;
rail.addEventListener(
  "touchstart",
  (e) => {
    if (!isMobile() || e.touches.length !== 1) return;
    touchY = e.touches[0].clientY;
  },
  { passive: true }
);
rail.addEventListener(
  "touchend",
  (e) => {
    if (!isMobile() || touchY == null) return;
    const dy = e.changedTouches[0].clientY - touchY;
    touchY = null;
    if (Math.abs(dy) < 56) return;
    // Don't steal scroll if the active sheet is mid-scroll
    const sheet = panels[index]?.querySelector(".sheet");
    if (sheet && sheet.scrollHeight > sheet.clientHeight + 8) {
      const atTop = sheet.scrollTop <= 2;
      const atBottom =
        sheet.scrollTop + sheet.clientHeight >= sheet.scrollHeight - 2;
      if (dy < 0 && !atBottom) return;
      if (dy > 0 && !atTop) return;
    }
    go(index + (dy < 0 ? 1 : -1));
  },
  { passive: true }
);

mobileMq.addEventListener("change", () => {
  applyLang();
  go(index, false);
});

applyLang();
rail.focus({ preventScroll: true });
