
import React from "react"
import {BrowserRouter , Routes , Route} from "react-router-dom"
import Home from "./pages/Home/Home"
import Contact from "./pages/Contact/Contact"
import About from "./pages/About/About"
import Layout from "./components/Layout"
import SearchPage from "./pages/Search/SearchPage"
import ProductPage from "./pages/Product/ProductPage"

function App() {

    return (
        <BrowserRouter>
            <Routes>
                <Route path="/" element={<Layout/>}>
                    <Route index element={<Home/>}/>
                    <Route path="about" element={<About/>}/>
                    <Route path="contact" element={<Contact/>}/>
                    <Route path="search" element={<SearchPage/>}/>
                    <Route path="product/:id" element={<ProductPage/>}/>
                </Route> 
            </Routes>
        </BrowserRouter>
    )
}

export default App
