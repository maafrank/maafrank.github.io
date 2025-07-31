// Generic script to mark a lesson as completed when user scrolls near bottom.
document.addEventListener('DOMContentLoaded', function () {
  const key = document.body.dataset.completeKey;
  if (!key) return;
  window.addEventListener('scroll', function () {
    if ((window.innerHeight + window.scrollY) >= document.body.offsetHeight - 100) {
      localStorage.setItem(key, 'true');
    }
  });
});
