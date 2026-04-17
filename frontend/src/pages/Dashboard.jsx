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

    if (loading) return (
        <div className="min-h-screen flex items-center justify-center bg-gradient-to-br from-slate-900 via-blue-950 to-slate-900">
            <div className="w-8 h-8 border-4 border-blue-400 border-t-transparent rounded-full animate-spin"></div>
        </div>
    )

    if (error) return (
        <div className="min-h-screen flex items-center justify-center bg-gradient-to-br from-slate-900 via-blue-950 to-slate-900 text-white">
            <p className="text-red-400 p-6">{error}</p>
        </div>
    )

    return (
        <div className="min-h-screen bg-gradient-to-br from-slate-900 via-blue-950 to-slate-900 text-white pb-10">

            <div className="absolute inset-0 opacity-10 pointer-events-none">
                <div className="absolute top-10 left-10 w-72 h-72 bg-blue-500 rounded-full blur-3xl"></div>
                <div className="absolute bottom-10 right-10 w-96 h-96 bg-purple-500 rounded-full blur-3xl"></div>
            </div>

            <div className="max-w-2xl mx-auto px-6 pt-10 relative z-10">
                <div className="flex justify-between items-center mb-8">
                    <h1 className="text-3xl font-black bg-gradient-to-r from-blue-400 to-indigo-400 bg-clip-text text-transparent">
                        Dashboard
                    </h1>
                    <button
                        onClick={() => navigate("/profile")}
                        className="flex items-center gap-2 text-sm text-blue-300 hover:text-white font-medium transition-colors bg-white/5 px-4 py-2 rounded-xl border border-white/10 hover:bg-white/10"
                    >
                        👤 Mi Perfil
                    </button>
                </div>

                {!data.level ? (
                    <div className="bg-white/5 backdrop-blur-sm border border-blue-500/30 p-8 rounded-2xl shadow-xl text-center">
                        <h2 className="text-2xl font-bold text-white mb-3">
                            ¡Bienvenido a EasyLearn!
                        </h2>
                        <p className="text-blue-200 mb-8 max-w-md mx-auto">
                            ¡Vamos a comprobar tu nivel para asignarte unos estudios adaptados a ti!
                        </p>
                        <button
                            onClick={() => navigate("/placement")}
                            className="bg-gradient-to-r from-blue-500 to-indigo-600 text-white px-8 py-3.5 rounded-xl font-semibold hover:from-blue-600 hover:to-indigo-700 transition-all shadow-lg shadow-blue-500/20 inline-block"
                        >
                            Empezar Test de Nivel
                        </button>
                    </div>
                ) : (
                    <div className="bg-white/5 backdrop-blur-sm border border-white/10 p-6 rounded-2xl shadow-xl">

                        <div className="grid grid-cols-2 gap-4 mb-8">
                            <div className="bg-white/5 rounded-xl p-4 border border-white/5">
                                <p className="text-gray-400 text-xs uppercase font-semibold mb-1">Nivel Actual</p>
                                <p className="text-2xl font-bold text-white">{data.level}</p>
                            </div>
                            <div className="bg-white/5 rounded-xl p-4 border border-white/5">
                                <p className="text-gray-400 text-xs uppercase font-semibold mb-1">Puntuación Test</p>
                                <p className="text-2xl font-bold text-white">{data.placement_score}</p>
                            </div>
                            <div className="bg-white/5 rounded-xl p-4 border border-white/5 col-span-2">
                                <p className="text-gray-400 text-xs uppercase font-semibold mb-1 flex justify-between">
                                    <span>Progreso General</span>
                                    <span>{data.completed_lessons} / {data.total_lessons} lecciones</span>
                                </p>
                                <p className="text-3xl font-bold text-white mb-2">{data.progress_percentage}%</p>
                                <div className="w-full bg-white/10 rounded-full h-2">
                                    <div
                                        className="bg-gradient-to-r from-blue-400 to-indigo-500 h-2 rounded-full transition-all duration-500"
                                        style={{ width: `${data.progress_percentage}%` }}
                                    ></div>
                                </div>
                            </div>
                        </div>

                        <button
                            onClick={() => navigate("/lessons")}
                            className="w-full bg-gradient-to-r from-blue-500 to-indigo-600 text-white font-bold py-3.5 rounded-xl hover:from-blue-600 hover:to-indigo-700 transition-all shadow-lg shadow-blue-500/20 mb-3"
                        >
                            Ir a mis lecciones
                        </button>

                        <button
                            onClick={() => navigate("/placement")}
                            className="w-full bg-white/5 border border-white/10 text-white font-medium py-3 rounded-xl hover:bg-white/10 transition-all"
                        >
                            Rehacer Test de Nivel
                        </button>

                    </div>
                )}
            </div>
        </div>
    )
}

export default Dashboard