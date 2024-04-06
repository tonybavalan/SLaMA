"use client"
import { useState } from "react"

const FileUpload = () => {

    const [file, setFile] = useState<string | undefined>();

    function handleChange(event: React.ChangeEvent<HTMLInputElement>) {
        if (event.target.files && event.target.files[0]) {
            setFile(event.target.files[0].name);
        }
    }

    return (
        <div className="flex items-center justify-center mt-6">
            <label className="border border-indigo-300 rounded-lg px-4 py-2" style={{
                background: 'linear-gradient(88.07deg, #C22ABA 2.49%, #4C34D8 100%)',
                padding: '10px 16px',
                color: '#FFFFFF',
                borderRadius: '20px'
            }}>
                <input type="file" accept=".csv, application/vnd.openxmlformats-officedocument.spreadsheetml.sheet, application/vnd.ms-excel, text/plain" onChange={handleChange} style={{ display: 'none' }} />
                {!file ? (
                    <span className="text-base text-gray-200">Upload File</span>
                ) : (
                    <span className="text-base text-gray-200">{file}</span>
                )}
            </label>
        </div>
    )
}

export default FileUpload;