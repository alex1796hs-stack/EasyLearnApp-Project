import api from "./api"

export const login = async (email, password) => {

    const params = new URLSearchParams()

    params.append("username", email)
    params.append("password", password)

    const response = await api.post(
        "/login",
        params,
        {
            headers: {
                "Content-Type": "application/x-www-form-urlencoded"
            }
        }
    )

    return response.data
}

export const register = async (email, password) => {
    const response = await api.post(
        "/register",
        {
            email,
            password
        }
    )

    return response.data
}