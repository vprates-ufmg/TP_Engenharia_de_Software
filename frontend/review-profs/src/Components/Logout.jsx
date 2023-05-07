import React from "react";
import Cookies from "js-cookie";

const Logout = _ => {
    async function handleLogout() {
        var session = Cookies.get("session")
        if (session === undefined){
          session = "";
        }

        const headers = new Headers();
        headers.append('Content-Type', 'application/json');
        const response = await fetch('http://127.0.0.1:5000/logout', {
          method: 'POST',
          headers: headers,
          body: JSON.stringify({session: session})
        })

        const data = await response.json()
        Cookies.remove("session")
        alert(data.message)

      };

      return (
        <button onClick={handleLogout}>Logout</button>
      )
}
  
export default Logout;
  