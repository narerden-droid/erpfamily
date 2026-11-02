import { useEffect, useState } from "react";

export default function App() {
  const [status, setStatus] = useState<string>("проверка…");

  useEffect(() => {
    fetch("/api/health")
      .then((r) => r.json())
      .then((d) => setStatus(d.status === "ok" ? "API работает" : "ошибка API"))
      .catch(() => setStatus("API недоступен"));
  }, []);

  return (
    <div className="min-h-screen flex items-center justify-center bg-slate-50">
      <div className="rounded-xl bg-white p-8 shadow">
        <h1 className="text-2xl font-semibold text-slate-800">Family ERP</h1>
        <p className="mt-2 text-slate-500">Статус: {status}</p>
      </div>
    </div>
  );
}
