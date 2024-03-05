function toggleDropdown() {
    const dropdown = document.querySelector('.dropdown');
    dropdown.classList.toggle('active');
  }
  
  function selectItem(item) {
    const dropdownToggle = document.querySelector('.dropdown-toggle');
    dropdownToggle.innerHTML = item;
    const dropdown = document.querySelector('.dropdown');
    dropdown.classList.remove('active');
  }
  