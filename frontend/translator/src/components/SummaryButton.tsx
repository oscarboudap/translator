import React, { useState } from 'react';

const SummaryButton: React.FC = () => {
    const [summary, setSummary] = useState<string>('');

    const fetchSummary = async () => {
        const response = await fetch('http://localhost:8000/summary');
        const data = await response.json();
        setSummary(data.summary);
    };

    return (
        <div>
            <button onClick={fetchSummary}>Generar Resumen</button>
            <div className="summary">{summary}</div>
        </div>
    );
};

export default SummaryButton;