/* Progressive enhancements; never persist or infer approvals. */
(() => {
  'use strict';
  const main = document.querySelector('main');
  if (!main) return;
  main.querySelectorAll('table').forEach(table => {
    const scroll = document.createElement('div');
    scroll.className = 'ux-table-scroll';
    scroll.setAttribute('role', 'region');
    scroll.setAttribute('aria-label', 'Tabla de datos; desplaza horizontalmente si es necesario');
    scroll.tabIndex = 0;
    table.before(scroll); scroll.append(table);
  });
  document.querySelectorAll('.fb textarea').forEach(t => t.setAttribute('aria-label', 'Comentario sobre esta pieza'));
  const overlay = document.getElementById('modal-overlay');
  let returnFocus = null;
  window.openPreview = button => {
    const piece = button.closest('article') || button.closest('details');
    if (!piece || !overlay) return;
    returnFocus = button;
    const clone = piece.cloneNode(true);
    clone.querySelectorAll('[id]').forEach(el => el.removeAttribute('id'));
    clone.removeAttribute('id');
    clone.querySelectorAll('.pv').forEach(el => el.remove());
    if (clone.matches('details')) clone.open = true;
    clone.querySelectorAll('details').forEach(el => el.open = true);
    document.getElementById('modal-body').replaceChildren(clone);
    overlay.classList.add('open');
    document.body.style.overflow = 'hidden';
    main.inert = true;
    document.querySelector('.nav').inert = true;
    overlay.querySelector('.modal-close').focus();
  };
  window.closePreview = () => {
    if (!overlay || !overlay.classList.contains('open')) return;
    overlay.classList.remove('open');
    document.getElementById('modal-body').replaceChildren();
    document.body.style.overflow = '';
    main.inert = false;
    document.querySelector('.nav').inert = false;
    returnFocus?.focus();
  };
  overlay?.addEventListener('keydown', e => {
    if (e.key !== 'Tab') return;
    const focusable = [...overlay.querySelectorAll('button, a[href], textarea, input, summary')].filter(el => el.getClientRects().length && !el.disabled);
    const first = focusable[0], last = focusable.at(-1);
    if (e.shiftKey && document.activeElement === first) { e.preventDefault(); last?.focus(); }
    else if (!e.shiftKey && document.activeElement === last) { e.preventDefault(); first?.focus(); }
  });
  const path = location.pathname.split('/').pop();
  if (path === 'calendario.html' || path === 'guiones.html' || path === 'graficas.html') {
    const container = path === 'calendario.html' ? main.querySelector('.cal') : path === 'graficas.html' ? main.querySelector('.grid') : main.querySelector('section .wrap');
    const items = [...container.children].filter(el => el.matches('article, details'));
    const controls = document.createElement('div');
    controls.className = 'ux-filters';
    controls.innerHTML = '<label>Buscar contenido<input type="search" placeholder="Tratamiento, título o fecha…" aria-label="Buscar contenido"></label><p class="ux-meta" role="status" aria-live="polite"></p>';
    if (path === 'guiones.html') items[0]?.before(controls); else container.before(controls);
    const input = controls.querySelector('input'), status = controls.querySelector('[role=status]');
    const norm = s => s.normalize('NFD').replace(/[\u0300-\u036f]/g, '').toLowerCase();
    const empty = document.createElement('p'); empty.className = 'ux-empty'; empty.hidden = true; empty.textContent = 'No hay coincidencias. Prueba otro tratamiento o título.'; container.after(empty);
    const filter = () => {
      let visible = 0;
      items.forEach(el => { el.hidden = !norm(el.textContent).includes(norm(input.value.trim())); if (!el.hidden) visible++; });
      status.textContent = `${visible} de ${items.length} piezas`; empty.hidden = visible > 0;
    };
    input.addEventListener('input', filter); filter();
  }
})();
