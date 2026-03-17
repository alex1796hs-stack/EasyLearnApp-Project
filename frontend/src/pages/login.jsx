import { useState } from "react"
import { login } from "../api/auth"

function Login() {

    const [username, setUsername] = useState("")
    const [password, setPassword] = useState("")

    const handleLogin = async (e) => {

        e.preventDefault()

        try {

            const data = await login(username, password)

            console.log("JWT:", data)

        } catch (error) {

            console.error("Login error:", error)

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

                <button className="w-full bg-blue-600 text-white p-2 rounded">
                    Login
                </button>

            </form>

        </div>

    )

}

export default Login