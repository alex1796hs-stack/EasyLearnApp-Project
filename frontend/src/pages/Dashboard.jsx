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

            <div className="bg-white p-4 rounded shadow">

                <p><strong>Level:</strong> {data.level}</p>
                <p><strong>Placement Score:</strong> {data.placement_score}</p>
                <p><strong>Completed Lessons:</strong> {data.completed_lessons}</p>
                <p><strong>Total Lessons:</strong> {data.total_lessons}</p>
                <p><strong>Progress:</strong> {data.progress_percentage}%</p>

            </div>

        </div>
    )
}

export default Dashboard