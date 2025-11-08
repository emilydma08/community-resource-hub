/* Put JS in here that applies to the entire site */

/* Nav Bar Hover JS */
document.addEventListener('DOMContentLoaded', () => {
  const directoryLink = document.querySelector('.group > a');
  const megaMenu = document.getElementById('mega-menu');

  if (!directoryLink || !megaMenu){
    return;
  }

  directoryLink.addEventListener('mouseenter', () => megaMenu.classList.remove('opacity-0','invisible','-translate-y-4'));
  directoryLink.addEventListener('mouseleave', () => megaMenu.classList.add('opacity-0','invisible','-translate-y-4'));

  megaMenu.addEventListener('mouseenter', () => megaMenu.classList.remove('opacity-0','invisible','-translate-y-4'));
  megaMenu.addEventListener('mouseleave', () => megaMenu.classList.add('opacity-0','invisible','-translate-y-4'));
});
