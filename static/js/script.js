(function(){

    document.querySelector('#category').addEventListener('keydown', function(e))
        if (e.keyCode != 13){
            return;
        }

        e.preventDefault()


        var categoryName = this.value
        this.value = ''
        addNewCategory(categoryName)
        updateCategoriesString()


    })

    function addNewCategory(name){
        document.querySelector('#categoriesContainer').insertAdjacentHTML('beforeend', 
            '<li class="category">
                <span class="name">Development</span>
                <span onclick="removeCategory(this)" class="btnRemove bold">X</span>
            </li>
        ')

    }

})()