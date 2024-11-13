// Function to load navbar.html and insert it into the #navbar div
function loadNavbar() {
  fetch('../components/navbar.html')
    .then((Response) => {
      if (!Response.ok) {
        throw new Error(
          'Something did not load correctly! Please reload the page'
        );
      }
      return Response.text();
    })
    .then((data) => {
      document.getElementById('navbar').innerHTML = data;
    })
    .catch((error) => console.error('Error loading navbar:', error));
}

// Call the function to load the navbar
loadNavbar();

// Function to load footer.html and insert it into the #footer div
function loadFooter() {
  fetch('../components/footer.html')
    .then((Response) => {
      if (!Response.ok) {
        throw new Error(
          'Something did not load correctly! Please reload the page'
        );
      }
      return Response.text();
    })
    .then((data) => {
      document.getElementById('footer').innerHTML = data;
    })
    .catch((error) => console.error('Error loading footer:', error));
}

// Call the function to load the footer
loadFooter();

function toggleMobileNav() {
  const mobileNav = document.getElementById('mobileNav');
  mobileNav.style.display =
    mobileNav.style.display === 'flex' ? 'none' : 'flex';
}
