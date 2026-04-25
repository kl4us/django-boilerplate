/**
 * CMS Navigation Handler - Multi-level support with optimized performance
 */
document.addEventListener('DOMContentLoaded', function () {
    const submenuToggles = document.querySelectorAll('.submenu-toggle');
    const mainNav = document.querySelectorAll('.navbar .dropdown');

    // Optimize: Cache parent selector to avoid repeated queries
    submenuToggles.forEach(function (toggle) {
        toggle.addEventListener('click', function (e) {
            e.preventDefault();
            e.stopPropagation();

            const nextSubmenu = this.nextElementSibling;
            
            if (nextSubmenu && nextSubmenu.classList.contains('dropdown-menu')) {
                const isOpen = nextSubmenu.classList.contains('show');
                const parent = this.closest('.dropdown-menu');
                
                if (parent) {
                    // Close sibling submenus efficiently
                    parent.querySelectorAll('.dropdown-menu.show').forEach(m => {
                        m.classList.remove('show');
                    });
                }

                if (!isOpen) {
                    nextSubmenu.classList.add('show');
                }
            }
        });
    });

    // Reset all submenus when main dropdown closes
    mainNav.forEach(function (dropdown) {
        dropdown.addEventListener('hidden.bs.dropdown', function () {
            this.querySelectorAll('.dropdown-menu.show').forEach(menu => {
                menu.classList.remove('show');
            });
        });
    });
});