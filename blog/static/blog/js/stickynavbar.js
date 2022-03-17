document.addEventListener("DOMContentLoaded", function(){
    window.addEventListener('scroll', function() {
        if (window.scrollY > 70) {
          document.getElementById('myTopnav').classList.add('fixed-top');
          // add padding top to show content behind navbar
          navbar_height = document.querySelector('.topnav').offsetHeight;
          document.body.style.paddingTop = navbar_height + 'px';
          document.getElementById('myTopnav').style.boxShadow = "0px 5px 5px -3px rgb(0 0 0 / 10%)";
        } else {
          document.getElementById('myTopnav').classList.remove('fixed-top');
           // remove padding top from body
          document.body.style.paddingTop = '0';
          document.getElementById('myTopnav').style.boxShadow = "0px 0px 0px 0px";
        } 
    });
  }); 
  // DOMContentLoaded  end