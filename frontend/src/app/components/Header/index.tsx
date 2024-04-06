import FileUpload from "../FileUpload";

const Header = () => {
    return (
        <div className="bg-gray-900 flex flex-col justify-center items-center text-center py-4">
            <p className="text-4xl font-bold text-gray-100">DY-DX DASHBOARD</p>
            <p className="text-base mt-2 text-gray-400">Enables users to upload files containing data and visualizes comprehensive reports through interactive charts</p>
            <FileUpload />
        </div>
    )
}

export default Header;