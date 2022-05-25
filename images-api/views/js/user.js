async function registration(login, password, email){
    const url_ = 'api/registration';
    const payload = {
        "login": login,
        "password": password,
        "email": email
    };

    const response = await fetch(url_, {
        method: 'POST',
        headers: {
            'Content-Type': 'application/json'
        },
        body: JSON.stringify(payload)
    });

    return response
}

async function regListener(){
    const emailField = document.getElementById("emailReg");
    const loginField = document.getElementById("loginReg");
    const passwordField = document.getElementById("passwdReg");
    response = await registration(loginField.value, passwordField.value, emailField.value);

    json_ = await response.json();
    statusCode = await response.status;
    if (statusCode == 200){
        const ref = "/"+json_.login;
        window.location.href = ref;
    }
    else{
        alert(json_.message)
    }
}

async function login(login, password){
    const url = "api/login";
    const payload = {
        "login": login,
        "password": password
    };

    const response = await fetch(url, {
        method: 'POST',
        headers: {
            'Content-Type': "application/json"
        },
        body: JSON.stringify(payload)
    });

    return response;
}

function setCookie(cname, cvalue, exdays) {
    const d = new Date();
    d.setTime(d.getTime() + (exdays*24*60*60*1000));
    let expires = "expires="+ d.toUTCString();
    document.cookie = cname + "=" + cvalue + ";" + expires + ";path=/";
}

async function loginListener(){
    const loginEmailField = document.getElementById("authLogin");
    const passwordEmailField = document.getElementById("authPasswd");
    response = await login(loginEmailField.value, passwordEmailField.value);

    json_ = await response.json();
    statusCode = await response.status;

    if (statusCode == 200){
        setCookie("imagesAuth", json_.Authorization, 100);
        window.location.href = "/";
    }
    else{
        alert(json_.message);
    }
    
}
