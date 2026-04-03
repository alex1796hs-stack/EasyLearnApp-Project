import { useState, useEffect } from "react"
import api from "../api/api"
import { useNavigate } from "react-router-dom"

function Dashboard() {

    const navigate = useNavigate()

    const [data, setData] = useState(null)
    const [loading, setLoading] = useState(true)
    const [error, setError] = useState("")

    useEffect(() => {

        const fetchDashboard = async () => {

            try {
                const response = await api.get("/dashboard")
                setData(response.data)

            } catch (err) {
                console.error(err)
                if (err.response?.status === 401) {
                    navigate("/login")
                } else {
                    setError("Error loading dashboard")
                }

            } finally {
                setLoading(false)
            }

        }

        fetchDashboard()

    }, [])

    if (loading) return <p className="p-6">Loading...</p>

    if (error) return <p className="p-6 text-red-500">{error}</p>

    return (
        <div className="p-6">

            <h1 className="text-2xl font-bold mb-4">
                Dashboard
            </h1>

            {!data.level ? (
                <div className="bg-blue-50 border-2 border-blue-200 p-6 rounded-xl shadow-sm text-center">
                    <h2 className="text-xl font-bold text-blue-800 mb-2">
                        ¡Bienvenido a EasyLearn!
                    </h2>
                    <p className="text-blue-600 mb-4">
                        ¡Vamos a comprobar tu nivel para asignarte unos estudios adaptados a ti!
                    </p>
                    <button 
                        onClick={() => navigate("/placement")}
                        className="bg-blue-600 text-white px-6 py-2 rounded-lg font-semibold hover:bg-blue-700 transition-colors"
                    >
                        Empezar Test de Nivel
                    </button>
                </div>
            ) : (
                <div className="bg-white p-4 rounded shadow">

                    <p><strong>Level:</strong> {data.level}</p>
                    <p><strong>Placement Score:</strong> {data.placement_score}</p>
                    <p><strong>Completed Lessons:</strong> {data.completed_lessons}</p>
                    <p><strong>Total Lessons:</strong> {data.total_lessons}</p>
                    <p><strong>Progress:</strong> {data.progress_percentage}%</p>
                    
                    <button 
                        onClick={() => navigate("/lessons")}
                        className="mt-6 w-full bg-blue-600 text-white font-bold py-3 rounded-lg hover:bg-blue-700 transition shadow"
                    >
                        🚀 Ir a mis lecciones
                    </button>

                    <button 
                        onClick={() => navigate("/placement")}
                        className="mt-3 w-full bg-gray-100 text-gray-700 font-medium py-2 rounded-lg hover:bg-gray-200 transition"
                    >
                        🔄 Rehacer Test de Nivel
                    </button>

                </div>
            )}

        </div>
    )
}

export default Dashboard