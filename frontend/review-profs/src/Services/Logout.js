const Logout = _ => {
    fetch('http://127.0.0.1:5000/logout')
        .then(response => response.json())
        .then(data => window.alert(data.message))
        .catch(error => console.log(error));
    
}

export default Logout