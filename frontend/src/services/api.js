const API_URL = "http://127.0.0.1:8000"

export async function login(email, password) {

  const res = await fetch(`${API_URL}/login`, {
    method: "POST",
    headers: {
      "Content-Type": "application/json"
    },
    body: JSON.stringify({ email, password })
  })

  return res.json()
}

export async function getUser() {

  const res = await fetch(`${API_URL}/me`, {
    headers: {
      "Authorization": "Bearer " + localStorage.getItem("token")
    }
  })

  return res.json()
}