'use strict';
document.querySelectorAll('[data-year]').forEach(el => { el.textContent = new Date().getFullYear(); });
const filterButtons = document.querySelectorAll('[data-filter]');
filterButtons.forEach(button => button.addEventListener('click', () => {
  filterButtons.forEach(item => { item.classList.toggle('active', item === button); item.setAttribute('aria-pressed', String(item === button)); });
  let count = 0;
  document.querySelectorAll('[data-category]').forEach(card => {
    card.hidden = button.dataset.filter !== 'all' && card.dataset.category !== button.dataset.filter;
    if (!card.hidden) count++;
  });
  document.getElementById('filter-status').textContent = `${count} services shown.`;
}));
// A direct service link must remain visible, including after filtering.
function revealService() {
  const card = document.getElementById(location.hash.slice(1));
  if (card && card.dataset.category && card.hidden) document.querySelector('[data-filter="all"]').click();
}
window.addEventListener('hashchange', revealService);
revealService();
const form = document.getElementById('brief-form');
if (form) {
  const service = new URLSearchParams(location.search).get('service');
  if (Array.from(form.elements.service.options).some(option => option.value === service)) form.elements.service.value = service;
  form.addEventListener('submit', event => {
    event.preventDefault();
    const values = new FormData(form);
    const name = values.get('name').trim();
    const message = values.get('message').trim();
    form.elements.name.setCustomValidity(name ? '' : 'Please enter your name.');
    form.elements.message.setCustomValidity(message.length >= 10 ? '' : 'Please describe your project in at least 10 characters.');
    if (!form.reportValidity()) return;
    document.getElementById('brief-output').value = `PROJECT BRIEF FOR ORBITIT SOLUTION LIMITED\n\nName: ${name}\nCompany: ${values.get('company').trim() || 'Not provided'}\nEmail: ${values.get('email').trim()}\nService: ${values.get('service')}\n\nProject overview:\n${message}`;
    document.getElementById('brief-result').hidden = false;
    document.getElementById('copy-status').textContent = '';
    document.getElementById('brief-output').focus();
  });
  ['name', 'message'].forEach(name => form.elements[name].addEventListener('input', () => form.elements[name].setCustomValidity('')));
  document.getElementById('copy-brief').addEventListener('click', async () => {
    const output = document.getElementById('brief-output');
    try {
      await navigator.clipboard.writeText(output.value);
      document.getElementById('copy-status').textContent = 'Brief copied. Nothing has been sent.';
    } catch {
      output.focus(); output.select();
      document.getElementById('copy-status').textContent = 'Select and copy the brief above using your keyboard or device menu.';
    }
  });
}
