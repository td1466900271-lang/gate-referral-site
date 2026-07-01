const REFERRAL_CODE = "VLYQB1HXUW";
const INVITE_URL = "https://www.gate.com/signup?ref=VLYQB1HXUW";
const OFFICIAL_PROMO_URL = "https://www.gate.com/referral";
const TELEGRAM_URL = "https://t.me/Gate_affiliate_offcial";

document.querySelectorAll("[data-invite]").forEach((link) => {
  link.setAttribute("href", INVITE_URL);
  link.setAttribute("target", "_blank");
  link.setAttribute("rel", "nofollow sponsored noopener");
});

document.querySelectorAll("[data-official]").forEach((link) => {
  link.setAttribute("href", OFFICIAL_PROMO_URL);
  link.setAttribute("target", "_blank");
  link.setAttribute("rel", "nofollow noopener");
});

document.querySelectorAll("[data-copy-code]").forEach((button) => {
  button.addEventListener("click", async () => {
    try {
      await navigator.clipboard.writeText(REFERRAL_CODE);
      const original = button.textContent;
      button.textContent = button.dataset.copied || "已复制";
      window.setTimeout(() => {
        button.textContent = original;
      }, 1600);
    } catch {
      window.prompt("Gate.io 邀请码", REFERRAL_CODE);
    }
  });
});

const tgLabels = {
  "zh-CN": "TG 联系",
  "zh-Hant": "TG 聯繫",
  en: "Telegram",
  ru: "Telegram",
};
const tgButton = document.createElement("a");
tgButton.className = "telegram-float";
tgButton.href = TELEGRAM_URL;
tgButton.target = "_blank";
tgButton.rel = "nofollow noopener";
tgButton.setAttribute("aria-label", "Telegram @Gate_affiliate_offcial");
tgButton.innerHTML = `<span class="telegram-icon">TG</span><span>${tgLabels[document.documentElement.lang] || "Telegram"}</span>`;
document.body.appendChild(tgButton);
