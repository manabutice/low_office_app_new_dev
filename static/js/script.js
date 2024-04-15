document.addEventListener('DOMContentLoaded', function() {
  // ページネーションのボタンにイベントリスナーを追加
  const pageButtons = document.querySelectorAll('.page-button');

  buttons.forEach(button => {
    button.addEventListener('mouseover', function() {
      this.style.backgroundColor = '#3e8e41';
    });

    button.addEventListener('mouseout', function() {
      this.style.backgroundColor = '#4CAF50';
    });

  pageButtons.forEach(button => {
      button.addEventListener('click', function(event) {
          const targetPage = this.getAttribute('data-page');
          window.location.href = `/users/${targetPage}`;
      });
    });
  });
});
