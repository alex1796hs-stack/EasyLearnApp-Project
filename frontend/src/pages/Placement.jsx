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

        const formattedAnswers = Object.entries(answers).map(([question_id, answer]) => ({
            question_id: parseInt(question_id, 10),
            answer
        }))

        if (formattedAnswers.length === 0) {
            alert("No has respondido ninguna pregunta. Por favor, selecciona alguna respuesta antes de enviar.")
            return
        }

        try {

            const res = await api.post("/placement/submit", {
                answers: formattedAnswers
            })

            setResult(res.data)

        } catch (err) {
            console.error(err)
        }

    }

    if (loading) return <p className="p-6">Loading test...</p>

    if (result) {
        return (
            <div className="p-6 max-w-2xl mx-auto">
                <div className="bg-white p-6 rounded-xl shadow-lg text-center mb-8 border-t-8 border-blue-600">
                    <h1 className="text-3xl font-bold text-gray-800">Tu nivel:</h1>
                    <p className="text-6xl font-black text-blue-600 my-4">{result.level}</p>
                    <p className="text-gray-500">Puntuación: {result.score}</p>
                </div>

                <div className="space-y-4">
                    <h2 className="text-xl font-bold text-gray-700 mb-4">Resumen del test:</h2>
                    {result.summary.map((item, idx) => (
                        <div key={idx} className={`p-4 rounded-lg border-l-4 ${item.is_correct ? 'bg-green-50 border-green-500' : 'bg-red-50 border-red-500'}`}>
                            <p className="font-medium text-gray-800 mb-2">{item.question}</p>
                            <div className="text-sm flex flex-col gap-1">
                                <p><span className="font-semibold">Tu respuesta:</span> {item.user_answer}</p>
                                {!item.is_correct && (
                                    <p className="text-green-700"><span className="font-semibold">Respuesta correcta:</span> {item.correct_answer}</p>
                                )}
                            </div>
                        </div>
                    ))}
                </div>

                <button
                    onClick={() => navigate("/dashboard")}
                    className="mt-8 bg-blue-600 text-white px-6 py-3 rounded-lg font-semibold hover:bg-blue-700 transition-colors"
                >
                    Ir al Dashboard →
                </button>
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
                            className={`block border p-2 mb-2 w-full text-left transition-colors ${answers[q.id] === opt ? "bg-blue-100 border-blue-500 font-medium" : "hover:bg-gray-50"
                                }`}
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