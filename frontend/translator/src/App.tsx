import React from 'react';
import Subtitles from './components/Subtitles';
import SummaryButton from './components/SummaryButton';

const App: React.FC = () => {
    return (
        <div>
            <h1>Traductor de Reuniones en Tiempo Real</h1>
            <Subtitles />
            <SummaryButton />
        </div>
    );
};

export default App;