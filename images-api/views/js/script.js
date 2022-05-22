$(function(){
    $('.minimized').click(function(event) {
      var i_path = $(this).attr('src');
      $('body').append('<div id="overlay"></div><div id="magnify"><img src="'+i_path+'"><div id="close-popup"><i></i></div></div>');
      $('#magnify').css({
       left: ($(document).width() - $('#magnify').outerWidth())/2,
       
              top: ($(window).height() - $('#magnify').outerHeight())/2
     });
      $('#overlay, #magnify').fadeIn('fast');
    });
    
    $('body').on('click', '#close-popup, #overlay', function(event) {
      event.preventDefault();
      $('#overlay, #magnify').fadeOut('fast', function() {
        $('#close-popup, #magnify, #overlay').remove();
      });
    });
  });

//  const url = 'http://localhost:8080/api/images/0ca40566-2a53-4f36-8c09-8e5872b81481';

  // const galleryContainer = document.getElementById('gallery')

  // function createImg(src){
  //   const imgBox = document.createElement('div')
  //   imgBox.classList.add('image-box')
  //   const img = document.createElement('img');
  //   img.classList.add('main-img','minimized');
  //   img.src = `${src}`;
  //   img.alt = `image`;
    
  //   galleryContainer.append(imgBox);
  //   imgBox.append(img)
  //  }

//  async function getData() {
//   const res = await fetch(url);
//   const data = await res.json();
//   console.log(data);
    
// }

 


//  getData();


 
