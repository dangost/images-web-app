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

    console.log(await response.json());
};

async function regListener(){
    const emailField = document.getElementById("emailReg");
    const loginField = document.getElementById("loginReg");
    const passwordField = document.getElementById("passwdReg");
    await registration(loginField.value, passwordField.value, emailField.value);
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

    return await response.json();
}

async function loginListener(){
    const loginEmailField = document.getElementById("authLogin");
    const passwordEmailField = document.getElementById("authPasswd");
    response = await login(loginEmailField.value, passwordEmailField.value);

    
    console.log(JSON.stringify(response));
}
