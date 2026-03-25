import { createContext, useState, useContext } from "react"
import { login as loginRequest } from "../api/auth"

export const AuthContext = createContext()

export const useAuth = () => useContext(AuthContext)

export const AuthProvider = ({ children }) => {

    const [token, setToken] = useState(localStorage.getItem("token"))

    const login = async (username, password) => {

        const data = await loginRequest(username, password)

        localStorage.setItem("token", data.access_token)

        setToken(data.access_token)

        return data
    }

    const logout = () => {
        localStorage.removeItem("token")
        setToken(null)
    }

    return (
        <AuthContext.Provider value={{ token, login, logout }}>
            {children}
        </AuthContext.Provider>
    )
}