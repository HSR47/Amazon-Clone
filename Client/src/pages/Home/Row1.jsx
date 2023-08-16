import Square from "./Square"
import styles from './Home.module.css'


function Row1(){

    let wishlist = {
        heading : "Wishlist",

        products : [
            {
                title : "Samsung Galaxy S20 FE 5G (Cloud Navy, 8GB RAM, 128GB Storage)",
                img : "https://m.media-amazon.com/images/I/81vDZyJQ-4L._AC_UY218_.jpg",
                url : "/"
            },
            {
                title : "Samsung Galaxy S20 FE 5G (Cloud Navy, 8GB RAM, 128GB Storage)",
                img : "https://m.media-amazon.com/images/I/81vDZyJQ-4L._AC_UY218_.jpg",
                url : "/"
            },
            {
                title : "Samsung Galaxy S20 FE 5G (Cloud Navy, 8GB RAM, 128GB Storage)",
                img : "https://m.media-amazon.com/images/I/81vDZyJQ-4L._AC_UY218_.jpg",
                url : "/"
            },
            {
                title : "Samsung Galaxy S20 FE 5G (Cloud Navy, 8GB RAM, 128GB Storage)",
                img : "https://m.media-amazon.com/images/I/81vDZyJQ-4L._AC_UY218_.jpg",
                url : "/"
            }
        ],

        link : {
            text : "Go to wishilist",
            href : "/"
        }
    }

    let cart = {
        heading : "Cart",

        products : [
            {
                title : "Samsung Galaxy S20 FE 5G (Cloud Navy, 8GB RAM, 128GB Storage)",
                img : "https://m.media-amazon.com/images/I/81vDZyJQ-4L._AC_UY218_.jpg",
                url : "/"
            },
            {
                title : "Samsung Galaxy S20 FE 5G (Cloud Navy, 8GB RAM, 128GB Storage)",
                img : "https://m.media-amazon.com/images/I/81vDZyJQ-4L._AC_UY218_.jpg",
                url : "/"
            },
            {
                title : "Samsung Galaxy S20 FE 5G (Cloud Navy, 8GB RAM, 128GB Storage)",
                img : "https://m.media-amazon.com/images/I/81vDZyJQ-4L._AC_UY218_.jpg",
                url : "/"
            },
            {
                title : "Samsung Galaxy S20 FE 5G (Cloud Navy, 8GB RAM, 128GB Storage)",
                img : "https://m.media-amazon.com/images/I/81vDZyJQ-4L._AC_UY218_.jpg",
                url : "/"
            }
        ],

        link : {
            text : "Go to cart",
            href : "/"
        }
    }

    let previouslyOrdered = {
        heading : "Previously Ordered",

        products : [
            {
                title : "Samsung Galaxy S20 FE 5G (Cloud Navy, 8GB RAM, 128GB Storage)",
                img : "https://m.media-amazon.com/images/I/81vDZyJQ-4L._AC_UY218_.jpg",
                url : "/"
            },
            {
                title : "Samsung Galaxy S20 FE 5G (Cloud Navy, 8GB RAM, 128GB Storage)",
                img : "https://m.media-amazon.com/images/I/81vDZyJQ-4L._AC_UY218_.jpg",
                url : "/"
            },
            {
                title : "Samsung Galaxy S20 FE 5G (Cloud Navy, 8GB RAM, 128GB Storage)",
                img : "https://m.media-amazon.com/images/I/81vDZyJQ-4L._AC_UY218_.jpg",
                url : "/"
            },
            {
                title : "Samsung Galaxy S20 FE 5G (Cloud Navy, 8GB RAM, 128GB Storage)",
                img : "https://m.media-amazon.com/images/I/81vDZyJQ-4L._AC_UY218_.jpg",
                url : "/"
            }
        ],

        link : {
            text : "order history",
            href : "/"
        }
    }
    return (
        <div className={styles.row1}>
            <Square info={wishlist}/>
            <Square info={cart}/>
            <Square info={previouslyOrdered}/>
        </div>
    )
}

export default Row1