import { useEffect, useState } from "react"
import api from "../api/api"

function LessonDetail() {

    const [lesson, setLesson] = useState(null)
    const [error, setError] = useState(null)
    const [currentQuestion, setCurrentQuestion] = useState(0)
    const [selected, setSelected] = useState(null)
    const [showAnswer, setShowAnswer] = useState(false)
    const [finished, setFinished] = useState(false)
    const [score, setScore] = useState(0)
    const [showPractice, setShowPractice] = useState(false)

    useEffect(() => {

        const fetchLesson = async () => {
            try {
                const res = await api.get("/lessons/next")
                setLesson(res.data)
            } catch (err) {
                console.error(err)
                if (err.response && err.response.status === 401) {
                    setError("Sesión caducada. Por favor, cierra sesión y vuelve a entrar.")
                } else {
                    setError("Error cargando la lección o no hay más lecciones.")
                }
            }
        }

        fetchLesson()

    }, [])

    if (error) return (
        <div className="text-center mt-10">
            <p className="text-red-500 font-bold text-xl">{error}</p>
            <button onClick={() => navigate("/dashboard")} className="mt-4 text-blue-500 underline">Volver al Dashboard</button>
        </div>
    )

    if (!lesson) return <p className="text-center mt-10">Loading...</p>

    if (!lesson.questions || lesson.questions.length === 0) {
        return <p className="text-center mt-10">No questions available</p>
    }

    const question = lesson.questions[currentQuestion]

    const handleAnswer = async (option) => {
        setSelected(option)
        setShowAnswer(true)

        const isCorrect = option === question.correct
        if (isCorrect) {
            setScore((prev) => prev + 1)
        }

        try {
            await api.post("/answers", {
                question_id: question.id,
                is_correct: isCorrect
            })
        } catch (err) {
            console.error("Error saving answer:", err)
        }
    }

    const nextQuestion = async () => {

        if (currentQuestion + 1 >= lesson.questions.length) {

            setFinished(true)

            try {
                await api.post(`/progress/${lesson.id}`)
            } catch (err) {
                console.error("Error saving progress:", err)
            }

            return
        }

        setCurrentQuestion(prev => prev + 1)
        setSelected(null)
        setShowAnswer(false)
    }

    if (finished) {
        const percentage = Math.round((score / lesson.questions.length) * 100)
        return (
            <div className="p-6 max-w-xl mx-auto text-center">
                <h1 className="text-2xl font-bold mb-4">{lesson.title}</h1>
                <p className="text-xl mb-2">🎉 ¡Lección completada!</p>
                <p className="text-lg">Puntuación: {score}/{lesson.questions.length} ({percentage}%)</p>
                <button
                    onClick={() => window.location.href = "/dashboard"}
                    className="mt-4 bg-blue-500 text-white px-4 py-2 rounded"
                >
                    Back to Dashboard
                </button>
            </div>
        )
    }

    if (!showPractice) {
        return (
            <div className="p-6 max-w-xl mx-auto">

                <h1 className="text-xl font-bold mb-4">
                    {lesson.title}
                </h1>

                {lesson.content && lesson.content.map((c, i) => (
                    <div key={i} className="mb-6">
                        <h2 className="font-semibold text-lg">{c.title}</h2>
                        <p className="text-gray-700 whitespace-pre-line">
                            {c.explanation}
                        </p>
                    </div>
                ))}

                <button
                    onClick={() => setShowPractice(true)}
                    className="bg-blue-500 text-white px-4 py-2 rounded"
                >
                    Start Practice
                </button>

            </div>
        )
    }

    return (
        <div className="p-6 max-w-xl mx-auto">

            <h1 className="text-xl font-bold mb-6">
                {lesson.title}
            </h1>

            <p className="mb-4 text-sm text-gray-500">
                Question {currentQuestion + 1} / {lesson.questions.length}
            </p>

            <p className="mb-4">
                {question.question}
            </p>

            <div className="space-y-3">
                {question.options.map((opt, i) => (
                    <button
                        key={i}
                        onClick={() => !showAnswer && handleAnswer(opt)}
                        className={`w-full p-2 border rounded ${showAnswer
                            ? opt === question.correct
                                ? "bg-green-200"
                                : opt === selected
                                    ? "bg-red-200"
                                    : ""
                            : ""
                            }`}
                    >
                        {opt}
                    </button>
                ))}
            </div>

            {showAnswer && (
                <button
                    onClick={nextQuestion}
                    className="mt-4 w-full bg-blue-500 text-white p-2 rounded"
                >
                    Next
                </button>
            )}

        </div>
    )
}

export default LessonDetail