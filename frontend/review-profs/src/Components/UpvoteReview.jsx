import Cookies from "js-cookie";

async function upvoteReview(review_id) {
  var session = Cookies.get("session");
  if (session === undefined) {
    session = "";
  }

  const headers = new Headers();
  headers.append("Content-Type", "application/json");
  const response = await fetch("http://127.0.0.1:5000/upvote_review", {
    method: "POST",
    headers: headers,
    body: JSON.stringify({ session: session, review_id: review_id }),
  });

  let data = await response.json();
  if (response.status == 403){
    Cookies.remove("session");
  }
  alert(data.message);
  return;
}
