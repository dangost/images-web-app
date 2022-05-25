function getCookie(cname) {
    let name = cname + "=";
    let decodedCookie = decodeURIComponent(document.cookie);
    let ca = decodedCookie.split(';');
    for(let i = 0; i <ca.length; i++) {
      let c = ca[i];
      while (c.charAt(0) == ' ') {
        c = c.substring(1);
      }
      if (c.indexOf(name) == 0) {
        return c.substring(name.length, c.length);
      }
    }
    return "";
}

const galleryContainer = document.getElementById('gallery');

function createImg(src){
    const imgBox = document.createElement('div')
    imgBox.classList.add('image-box')
    const img = document.createElement('img');
    img.classList.add('main-img','minimized');
    img.width = 500;
    img.height = 500;
    img.src = `${src}`;
    img.alt = `image`;

    galleryContainer.append(imgBox);
    imgBox.append(img)
}


async function getMe(){
    const token = getCookie("imagesAuth");
    if (!token){
      location.href = "/signup";
    }
    const response = await fetch("api/me", {
      headers: {
        "Authorization": token
      }
    });
    return response;
}

function getTableString(image){
    if (image == undefined){
      return '<th></th>'
    }
    return '<th><a href="'+ image.source + '"><img src="'+ image.source + '" height="300"></a><figcaption>'+ image.description + '</figcaption></th>'
}

async function initPage(){

    const hello = document.getElementById("loginField");

    response = await getMe();

    const json_ = await response.json();
    const login = json_.login;

    hello.innerHTML = "Hello, " + login + "!";

    appending = "";
    for (let i = 0; i < json_.images.length; i += 4){
        appending += "<tr>";
        for (let q = i; q < i+4; q++){
          appending += getTableString(json_.images[q]);
        }
        appending += "</tr>";
    }

    $('#mainTableFoot').append(appending);

    // <tr>
    //   <th><a href=""><img src="" width="500"></a><figcaption>Cat</figcaption></th>
    // </tr>
}

initPage();

