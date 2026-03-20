import { useState, useEffect } from "react"
import api from "../api/api"
import { useNavigate } from "react-router-dom"

function Placement() {

    const [questions, setQuestions] = useState([])
    const [answers, setAnswers] = useState({})
    const [loading, setLoading] = useState(true)
    const [result, setResult] = useState(null)
    const navigate = useNavigate()

    // 🟢 cargar preguntas
    useEffect(() => {

        const startPlacement = async () => {
            try {
                const res = await api.post("/placement/start")
                setQuestions(res.data.questions)
            } catch (err) {
                console.error(err)
            } finally {
                setLoading(false)
            }
        }

        startPlacement()

    }, [])

    // 🟡 guardar respuesta
    const handleAnswer = (questionId, value) => {
        setAnswers({
            ...answers,
            [questionId]: value
        })
    }

    // 🔵 enviar test
    const handleSubmit = async () => {

        try {

            const res = await api.post("/placement/submit", {
                answers
            })

            setResult(res.data)

            // redirigir después de 2s
            setTimeout(() => {
                navigate("/dashboard")
            }, 2000)

        } catch (err) {
            console.error(err)
        }

    }

    if (loading) return <p className="p-6">Loading test...</p>

    if (result) {
        return (
            <div className="p-6">
                <h1 className="text-2xl font-bold">Your level:</h1>
                <p className="text-xl mt-2">{result.level}</p>
            </div>
        )
    }

    return (

        <div className="p-6">

            <h1 className="text-2xl font-bold mb-6">
                Placement Test
            </h1>

            {questions.map((q) => (

                <div key={q.id} className="mb-6">

                    <p className="mb-2">{q.question}</p>

                    {q.options.map((opt) => (

                        <button
                            key={opt}
                            onClick={() => handleAnswer(q.id, opt)}
                            className="block border p-2 mb-2 w-full text-left"
                        >
                            {opt}
                        </button>

                    ))}

                </div>

            ))}

            <button
                onClick={handleSubmit}
                className="bg-blue-600 text-white px-4 py-2 rounded"
            >
                Submit
            </button>

        </div>

    )
}

export default Placement