import React from "react";
import Cookies from "js-cookie";

const Logout = _ => {
    async function handleLogout() {
        const response = await fetch('http://127.0.0.1:5000/logout', {
          method: 'GET',
        })
        const data = await response.json()
        
        if (data.success) {
            Cookies.remove("current_session");
            alert("Usuário desconectado")
        }
        else {
            alert(data.message)
        }
      };

      return (
        <button onClick={handleLogout}>Logout</button>
      )
}
  
export default Logout;
  