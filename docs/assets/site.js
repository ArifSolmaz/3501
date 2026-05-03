(function () {
  const canvas = document.getElementById("starfield");
  if (!canvas) return;

  const ctx = canvas.getContext("2d", { alpha: false });
  const prefersReducedMotion = window.matchMedia("(prefers-reduced-motion: reduce)").matches;
  let stars = [];
  let width = 0;
  let height = 0;
  let animationFrame = null;

  function resize() {
    const ratio = Math.min(window.devicePixelRatio || 1, 2);
    width = window.innerWidth;
    height = window.innerHeight;
    canvas.width = Math.floor(width * ratio);
    canvas.height = Math.floor(height * ratio);
    canvas.style.width = width + "px";
    canvas.style.height = height + "px";
    ctx.setTransform(ratio, 0, 0, ratio, 0, 0);

    const count = Math.max(120, Math.floor((width * height) / 8200));
    stars = Array.from({ length: count }, function () {
      return {
        x: Math.random() * width,
        y: Math.random() * height,
        r: Math.random() * 1.1 + 0.2,
        a: Math.random() * 0.65 + 0.2,
        drift: Math.random() * 0.18 + 0.02
      };
    });
  }

  function draw() {
    ctx.fillStyle = "#030308";
    ctx.fillRect(0, 0, width, height);

    const gradient = ctx.createLinearGradient(0, 0, width, height);
    gradient.addColorStop(0, "rgba(74, 158, 255, 0.10)");
    gradient.addColorStop(0.45, "rgba(3, 3, 8, 0.0)");
    gradient.addColorStop(1, "rgba(255, 212, 117, 0.08)");
    ctx.fillStyle = gradient;
    ctx.fillRect(0, 0, width, height);

    for (const star of stars) {
      ctx.beginPath();
      ctx.arc(star.x, star.y, star.r, 0, Math.PI * 2);
      ctx.fillStyle = "rgba(231, 232, 243, " + star.a + ")";
      ctx.fill();

      if (!prefersReducedMotion) {
        star.y += star.drift;
        if (star.y > height + 2) {
          star.y = -2;
          star.x = Math.random() * width;
        }
      }
    }

    if (!prefersReducedMotion) {
      animationFrame = window.requestAnimationFrame(draw);
    }
  }

  function markActiveNav() {
    const current = window.location.pathname.split("/").pop() || "index.html";
    document.querySelectorAll(".site-nav a").forEach(function (link) {
      const target = link.getAttribute("href");
      if (target === current) {
        link.classList.add("is-active");
        link.setAttribute("aria-current", "page");
        link.scrollIntoView({ block: "nearest", inline: "center" });
      }
    });
  }

  window.addEventListener("resize", function () {
    if (animationFrame) window.cancelAnimationFrame(animationFrame);
    resize();
    draw();
  });

  resize();
  draw();
  markActiveNav();
})();
