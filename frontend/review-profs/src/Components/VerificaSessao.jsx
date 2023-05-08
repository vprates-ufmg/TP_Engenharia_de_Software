import Cookies from "js-cookie";

async function verificaSessao() {
  var session = Cookies.get("session");
  if (session === undefined) {
    return false;
  }

  const headers = new Headers();
  headers.append("Content-Type", "application/json");
  const response = await fetch("http://127.0.0.1:5000/verifica_sessao", {
    method: "POST",
    headers: headers,
    body: JSON.stringify({ session: session }),
  });

  const data = await response.json();
  if (data.success) {
    Cookies.set("session", data.session);
    return true;
  } else {
    Cookies.remove("session");
    return false;
  }
}
