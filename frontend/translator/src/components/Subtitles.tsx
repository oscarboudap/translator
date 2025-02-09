import React, { useState, useEffect } from 'react';

const Subtitles: React.FC = () => {
    const [subtitle, setSubtitle] = useState<string>('');

    useEffect(() => {
        const socket = new WebSocket('ws://localhost:8000/ws');

        socket.onmessage = (event) => {
            setSubtitle(event.data);
        };

        return () => socket.close();
    }, []);

    return <div className="subtitles">{subtitle}</div>;
};

export default Subtitles;