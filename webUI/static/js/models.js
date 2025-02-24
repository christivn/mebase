async function getModelsJSON(url) {
    try {
        const response = await fetch(url);
        if (!response.ok) {
            throw new Error(`Error al obtener los datos: ${response.statusText}`);
        }
        
        const data = await response.json();
        const timestamp = new Date().toISOString();
        
        localStorage.setItem('models_jsonData', JSON.stringify({ data, timestamp }));
        console.log('Datos guardados en localStorage', { data, timestamp });
    } catch (error) {
        console.error('Error:', error);
    }
}

function getStoredModelsJSON() {
    const storedData = localStorage.getItem('models_jsonData');
    if (storedData) {
        return JSON.parse(storedData);
    }
    return null;
}

// Uso del script
const url = './get-models';
if (localStorage.getItem('models_jsonData') == null){ 
    getModelsJSON(url);
} else {
    // Para recuperar los datos guardados
    const allModels =  getStoredModelsJSON();

    // Comprueba si el localStorage de los models tiene más de 60min
    const timestampDate = new Date(allModels.timestamp);
    const oneHourAgo = new Date(Date.now() - 60 * 60 * 1000); // Resta una hora al tiempo actual
    // Si es de hace más de una hora se actualiza
    if(timestampDate < oneHourAgo){ getModelsJSON(url); }
}