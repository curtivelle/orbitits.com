'use strict';
document.querySelectorAll('[data-year]').forEach(el => el.textContent = new Date().getFullYear());
const filters = document.querySelectorAll('[data-filter]');
filters.forEach(button => button.addEventListener('click', () => {
  filters.forEach(item => { item.classList.toggle('active',item === button); item.setAttribute('aria-pressed', String(item === button)); });
  let visible = 0;
  document.querySelectorAll('[data-category]').forEach(card => { card.hidden = button.dataset.filter !== 'All' && card.dataset.category !== button.dataset.filter; if (!card.hidden) visible++; });
  const status = document.querySelector('[data-filter-status]');
  if (status) status.textContent = `${visible} items shown.`;
}));
function revealAnchor() {
  const target = document.getElementById(location.hash.slice(1));
  if (target && target.closest('[data-category]')?.hidden) {
    document.querySelector('[data-filter="All"]')?.click();
    target.scrollIntoView({block:'start'});
  }
}
window.addEventListener('hashchange',revealAnchor); revealAnchor();
const form = document.getElementById('enquiry-form');
if (form) {
  const status = document.getElementById('form-status');
  const params = new URLSearchParams(location.search);
  for (const key of ['service','package']) {
    const value = params.get(key);
    if (value && [...form.elements[key].options].some(option => option.value === value)) form.elements[key].value = value;
  }
  const notify = (text,type='') => {status.textContent = text;status.className = `form-status ${type}`;};
  function valid() {
    form.elements.name.setCustomValidity(form.elements.name.value.trim() ? '' : 'Please enter your name.');
    form.elements.message.setCustomValidity(form.elements.message.value.trim().length >= 10 ? '' : 'Please describe your project in at least 10 characters.');
    return form.reportValidity();
  }
  for (const name of ['name','message']) form.elements[name].addEventListener('input',() => form.elements[name].setCustomValidity(''));
  function prepareEmail() {
    if (!valid()) return;
    const values = new FormData(form);
    const packageText = form.elements.package.selectedOptions[0].textContent;
    const brief = `ORBITIT PROJECT ENQUIRY\n\nName: ${values.get('name').trim()}\nCompany: ${values.get('company').trim() || 'Not provided'}\nReply email: ${values.get('email').trim()}\nService: ${values.get('service')}\nPackage: ${packageText}\n\nProject:\n${values.get('message').trim()}`;
    document.getElementById('email-brief').value = brief;
    document.getElementById('email-link').href = `mailto:robi@orbitits.com?subject=${encodeURIComponent('Project enquiry — OrbitIT')}&body=${encodeURIComponent(brief)}`;
    document.getElementById('email-fallback').hidden = false;
    document.getElementById('email-brief').focus();
    notify('Your enquiry is prepared. Nothing has been sent. Open your email app to review and send it.');
  }
  document.getElementById('prepare-email').addEventListener('click',prepareEmail);
  document.getElementById('copy-enquiry').addEventListener('click', async () => {
    const output = document.getElementById('email-brief');
    try { await navigator.clipboard.writeText(output.value); notify('Enquiry copied. Nothing has been sent.'); }
    catch { output.focus(); output.select(); notify('Copy the selected enquiry using your keyboard or device menu.'); }
  });
  form.addEventListener('submit', event => {
    event.preventDefault();
    if (!valid()) return;
    const values = new FormData(form);
    const packageText = form.elements.package.selectedOptions[0].textContent;
    const message = `ORBITIT PROJECT ENQUIRY\n\nName: ${values.get('name').trim()}\nCompany: ${values.get('company').trim() || 'Not provided'}\nReply email: ${values.get('email').trim()}\nService: ${values.get('service')}\nPackage: ${packageText}\n\nProject:\n${values.get('message').trim()}`;
    const url = `https://wa.me/447466741958?text=${encodeURIComponent(message)}`;
    document.getElementById('whatsapp-link').href = url;
    document.getElementById('whatsapp-fallback').hidden = false;
    notify('Your WhatsApp message is prepared. Review it and press Send in WhatsApp. Nothing has been sent automatically.');
    window.open(url, '_blank', 'noopener,noreferrer');
  });
}
