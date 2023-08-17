import ProductSlider from "./ProductSlider"
import styles from './Home.module.css'


function Products() {

    let info = {
        heading: "newly added products",
        products: [
            {
                title: "boAt Rockerz 370 On Ear Bluetooth Headphones with Upto 12 Hours Playtime",
                price: 1099,
                images: [
                    "https://m.media-amazon.com/images/I/61kWB+uzR2L._AC_SY175_.jpg",
                    "https://m.media-amazon.com/images/I/51i+LdztEBL._AC_SY175_.jpg",
                    "https://m.media-amazon.com/images/I/61mqICk0GKL._AC_SY175_.jpg",
                    "https://m.media-amazon.com/images/I/61WqF8Y6HTL._AC_SY175_.jpg"
                ]
            },
            {
                title: "boAt Rockerz 370 On Ear Bluetooth Headphones with Upto 12 Hours Playtime",
                price: 1099,
                images: [
                    "https://m.media-amazon.com/images/I/61kWB+uzR2L._AC_SY175_.jpg",
                    "https://m.media-amazon.com/images/I/51i+LdztEBL._AC_SY175_.jpg",
                    "https://m.media-amazon.com/images/I/61mqICk0GKL._AC_SY175_.jpg",
                    "https://m.media-amazon.com/images/I/61WqF8Y6HTL._AC_SY175_.jpg"
                ]
            },
            {
                title: "boAt Rockerz 370 On Ear Bluetooth Headphones with Upto 12 Hours Playtime",
                price: 1099,
                images: [
                    "https://m.media-amazon.com/images/I/61kWB+uzR2L._AC_SY175_.jpg",
                    "https://m.media-amazon.com/images/I/51i+LdztEBL._AC_SY175_.jpg",
                    "https://m.media-amazon.com/images/I/61mqICk0GKL._AC_SY175_.jpg",
                    "https://m.media-amazon.com/images/I/61WqF8Y6HTL._AC_SY175_.jpg"
                ]
            },
            {
                title: "boAt Rockerz 370 On Ear Bluetooth Headphones with Upto 12 Hours Playtime",
                price: 1099,
                images: [
                    "https://m.media-amazon.com/images/I/61kWB+uzR2L._AC_SY175_.jpg",
                    "https://m.media-amazon.com/images/I/51i+LdztEBL._AC_SY175_.jpg",
                    "https://m.media-amazon.com/images/I/61mqICk0GKL._AC_SY175_.jpg",
                    "https://m.media-amazon.com/images/I/61WqF8Y6HTL._AC_SY175_.jpg"
                ]
            },
            {
                title: "boAt Rockerz 370 On Ear Bluetooth Headphones with Upto 12 Hours Playtime",
                price: 1099,
                images: [
                    "https://m.media-amazon.com/images/I/61kWB+uzR2L._AC_SY175_.jpg",
                    "https://m.media-amazon.com/images/I/51i+LdztEBL._AC_SY175_.jpg",
                    "https://m.media-amazon.com/images/I/61mqICk0GKL._AC_SY175_.jpg",
                    "https://m.media-amazon.com/images/I/61WqF8Y6HTL._AC_SY175_.jpg"
                ]
            },
            {
                title: "boAt Rockerz 370 On Ear Bluetooth Headphones with Upto 12 Hours Playtime",
                price: 1099,
                images: [
                    "https://m.media-amazon.com/images/I/61kWB+uzR2L._AC_SY175_.jpg",
                    "https://m.media-amazon.com/images/I/51i+LdztEBL._AC_SY175_.jpg",
                    "https://m.media-amazon.com/images/I/61mqICk0GKL._AC_SY175_.jpg",
                    "https://m.media-amazon.com/images/I/61WqF8Y6HTL._AC_SY175_.jpg"
                ]
            },
            {
                title: "boAt Rockerz 370 On Ear Bluetooth Headphones with Upto 12 Hours Playtime",
                price: 1099,
                images: [
                    "https://m.media-amazon.com/images/I/61kWB+uzR2L._AC_SY175_.jpg",
                    "https://m.media-amazon.com/images/I/51i+LdztEBL._AC_SY175_.jpg",
                    "https://m.media-amazon.com/images/I/61mqICk0GKL._AC_SY175_.jpg",
                    "https://m.media-amazon.com/images/I/61WqF8Y6HTL._AC_SY175_.jpg"
                ]
            },
            {
                title: "boAt Rockerz 370 On Ear Bluetooth Headphones with Upto 12 Hours Playtime",
                price: 1099,
                images: [
                    "https://m.media-amazon.com/images/I/61kWB+uzR2L._AC_SY175_.jpg",
                    "https://m.media-amazon.com/images/I/51i+LdztEBL._AC_SY175_.jpg",
                    "https://m.media-amazon.com/images/I/61mqICk0GKL._AC_SY175_.jpg",
                    "https://m.media-amazon.com/images/I/61WqF8Y6HTL._AC_SY175_.jpg"
                ]
            },
            {
                title: "boAt Rockerz 370 On Ear Bluetooth Headphones with Upto 12 Hours Playtime",
                price: 1099,
                images: [
                    "https://m.media-amazon.com/images/I/61kWB+uzR2L._AC_SY175_.jpg",
                    "https://m.media-amazon.com/images/I/51i+LdztEBL._AC_SY175_.jpg",
                    "https://m.media-amazon.com/images/I/61mqICk0GKL._AC_SY175_.jpg",
                    "https://m.media-amazon.com/images/I/61WqF8Y6HTL._AC_SY175_.jpg"
                ]
            },
            {
                title: "boAt Rockerz 370 On Ear Bluetooth Headphones with Upto 12 Hours Playtime",
                price: 1099,
                images: [
                    "https://m.media-amazon.com/images/I/61kWB+uzR2L._AC_SY175_.jpg",
                    "https://m.media-amazon.com/images/I/51i+LdztEBL._AC_SY175_.jpg",
                    "https://m.media-amazon.com/images/I/61mqICk0GKL._AC_SY175_.jpg",
                    "https://m.media-amazon.com/images/I/61WqF8Y6HTL._AC_SY175_.jpg"
                ]
            },
            {
                title: "boAt Rockerz 370 On Ear Bluetooth Headphones with Upto 12 Hours Playtime",
                price: 1099,
                images: [
                    "https://m.media-amazon.com/images/I/61kWB+uzR2L._AC_SY175_.jpg",
                    "https://m.media-amazon.com/images/I/51i+LdztEBL._AC_SY175_.jpg",
                    "https://m.media-amazon.com/images/I/61mqICk0GKL._AC_SY175_.jpg",
                    "https://m.media-amazon.com/images/I/61WqF8Y6HTL._AC_SY175_.jpg"
                ]
            },
            {
                title: "boAt Rockerz 370 On Ear Bluetooth Headphones with Upto 12 Hours Playtime",
                price: 1099,
                images: [
                    "https://m.media-amazon.com/images/I/61kWB+uzR2L._AC_SY175_.jpg",
                    "https://m.media-amazon.com/images/I/51i+LdztEBL._AC_SY175_.jpg",
                    "https://m.media-amazon.com/images/I/61mqICk0GKL._AC_SY175_.jpg",
                    "https://m.media-amazon.com/images/I/61WqF8Y6HTL._AC_SY175_.jpg"
                ]
            },
            {
                title: "boAt Rockerz 370 On Ear Bluetooth Headphones with Upto 12 Hours Playtime",
                price: 1099,
                images: [
                    "https://m.media-amazon.com/images/I/61kWB+uzR2L._AC_SY175_.jpg",
                    "https://m.media-amazon.com/images/I/51i+LdztEBL._AC_SY175_.jpg",
                    "https://m.media-amazon.com/images/I/61mqICk0GKL._AC_SY175_.jpg",
                    "https://m.media-amazon.com/images/I/61WqF8Y6HTL._AC_SY175_.jpg"
                ]
            },
            
        ]
    }


    return (
        <>
            <ProductSlider info={info}/>
            <ProductSlider info={info}/>
            <ProductSlider info={info}/>
        </>
        
    )
}

export default Products