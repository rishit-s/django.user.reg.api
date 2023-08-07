const show = () => {
    let password = document.getElementById(password);
    let visibility = document.querySelector(".visibility");
    if(password.type === "password"){
        password.type = "text";
        visibility.style.color="#ccc";

    }else{
        password.type = "password";
        visibility.style.color="#fff"
    }
}