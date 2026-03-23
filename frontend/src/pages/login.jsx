import { useState, useEffect } from "react"
import { useContext } from "react"
import { AuthContext } from "../context/AuthContext"
import { useNavigate } from "react-router-dom"
import api from "../api/api"

function Login() {
    const { login } = useContext(AuthContext)
    const [username, setUsername] = useState("")
    const [password, setPassword] = useState("")
    const [error, setError] = useState(null)
    const [isLoading, setIsLoading] = useState(false)
    const navigate = useNavigate()

    const handleLogin = async (e) => {

        e.preventDefault()

        setIsLoading(true)
        setError(null)

        try {

            await login(username, password)
            
            // Ya el token fue guardado por AuthContext.login
            
            // Obtener datos del dashboard para ver si hay level
            const res = await api.get("/dashboard")
            
            if (!res.data.level) {
                navigate("/placement")
            } else {
                navigate("/dashboard")
            }

        } catch (err) {

            console.error("Login error:", err)
            setError(err.response?.data?.message || err.message || "Credenciales incorrectas")

        } finally {
            setIsLoading(false)
        }

    }

    return (

        <div className="min-h-screen flex items-center justify-center bg-gray-100">

            <form
                onSubmit={handleLogin}
                className="bg-white p-8 rounded-xl shadow w-full max-w-sm"
            >

                <h1 className="text-2xl font-bold mb-6 text-center">
                    EasyLearn
                </h1>

                {error && (
                    <p className="text-red-500 text-sm mb-4 text-center">
                        {error}
                    </p>
                )}

                <input
                    type="text"
                    placeholder="Username"
                    value={username}
                    onChange={(e) => setUsername(e.target.value)}
                    className="w-full border p-2 rounded mb-4"
                />

                <input
                    type="password"
                    placeholder="Password"
                    value={password}
                    onChange={(e) => setPassword(e.target.value)}
                    className="w-full border p-2 rounded mb-4"
                />

                <button
                    disabled={isLoading}
                    className="w-full bg-blue-600 text-white p-2 rounded disabled:opacity-75 flex items-center justify-center transition-colors hover:bg-blue-700"
                >
                    {isLoading ? (
                        <>
                            <svg className="animate-spin -ml-1 mr-2 h-5 w-5 text-white" xmlns="http://www.w3.org/2000/svg" fill="none" viewBox="0 0 24 24">
                                <circle className="opacity-25" cx="12" cy="12" r="10" stroke="currentColor" strokeWidth="4"></circle>
                                <path className="opacity-75" fill="currentColor" d="M4 12a8 8 0 018-8V0C5.373 0 0 5.373 0 12h4zm2 5.291A7.962 7.962 0 014 12H0c0 3.042 1.135 5.824 3 7.938l3-2.647z"></path>
                            </svg>
                            Loading...
                        </>
                    ) : (
                        "Login"
                    )}
                </button>

            </form>

        </div>

    )

}

export default Login