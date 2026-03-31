import { useEffect, useState } from "react"
import { useNavigate } from "react-router-dom"
import api from "../api/api"

function Lessons() {

    const [lessons, setLessons] = useState([])
    const [loading, setLoading] = useState(true)
    const [error, setError] = useState(null)

    const navigate = useNavigate()

    useEffect(() => {

        const fetchLessons = async () => {
            try {
                const res = await api.get("/lessons")
                setLessons(res.data)
            } catch (err) {
                console.error(err)
                setError("Error loading lessons")
            } finally {
                setLoading(false)
            }
        }

        fetchLessons()

    }, [])

    if (loading) return <p className="text-center mt-10">Loading lessons...</p>
    if (error) return <p className="text-center text-red-500">{error}</p>

    return (
        <div className="p-6">

            <h1 className="text-3xl font-bold mb-6 text-center">
                Your Lessons
            </h1>

            <div className="grid gap-6 md:grid-cols-2">

                {lessons.map((lesson) => (
                    <div
                        key={lesson.id}
                        onClick={() => navigate("/lesson")}
                        className="p-6 bg-white rounded-xl shadow hover:shadow-lg cursor-pointer transition"
                    >
                        <h2 className="text-xl font-semibold mb-2">
                            {lesson.title}
                        </h2>

                        <p className="text-sm text-gray-500 capitalize">
                            {lesson.type}
                        </p>
                    </div>
                ))}

            </div>

        </div>
    )
}

export default Lessons