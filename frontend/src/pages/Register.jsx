import { useState } from "react"
import { useNavigate, Link } from "react-router-dom"
import { register } from "../api/auth"

const Register = () => {
    const [email, setEmail] = useState("")
    const [password, setPassword] = useState("")
    const navigate = useNavigate()

    const [error, setError] = useState(null)

    const handleSubmit = async (e) => {
        e.preventDefault()
        setError(null)

        try {
            await register(email, password)
            navigate("/login")
        } catch (error) {
            console.error(error)
            const detail = error.response?.data?.detail
            if (Array.isArray(detail)) {
                setError(detail.map(err => `${err.loc[1]}: ${err.msg}`).join(", "))
            } else {
                setError(detail || "Error registering user")
            }
        }
    }

    return (
        <div className="min-h-screen flex items-center justify-center bg-gray-100">
            <form onSubmit={handleSubmit} className="bg-white p-6 rounded shadow-md w-80">
                <h2 className="text-xl font-bold mb-4">Register</h2>

                {error && (
                    <p className="text-red-500 text-sm mb-4 text-center bg-red-50 p-2 rounded border border-red-200">
                        {error}
                    </p>
                )}

                <input
                    type="email"
                    placeholder="Email"
                    className="w-full mb-3 p-2 border"
                    value={email}
                    onChange={(e) => setEmail(e.target.value)}
                />

                <input
                    type="password"
                    placeholder="Password"
                    className="w-full mb-3 p-2 border"
                    value={password}
                    onChange={(e) => setPassword(e.target.value)}
                />

                <button className="w-full bg-blue-500 text-white p-2">
                    Register
                </button>

                <p className="mt-4 text-center text-sm text-gray-600">
                    ¿Ya tienes una cuenta?{" "}
                    <Link to="/login" className="text-blue-600 hover:underline">
                        Inicia sesión
                    </Link>
                </p>
            </form>
        </div>
    )
}

export default Register