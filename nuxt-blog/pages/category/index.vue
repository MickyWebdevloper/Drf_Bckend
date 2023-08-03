<script setup>
/* Navigation will occur before fetching is complete.
  Handle pending and error states directly within your component's template
*/
const { pending, error, data: categories
} = await useLazyAsyncData('data', () => $fetch('http://localhost:8000/api/category/'));
console.log('Hello', categories)
console.log('pending', pending)
console.log('error', error)
// watch(count, (newCount) => {
    // Because count might start out null, you won't have access
    // to its contents immediately, but you can watch it.
// })
</script> 

<template>
    <div>
        <section class="text-gray-600 body-font">
            <div class="flex flex-wrap sm:-m-4 -mx-4 -mb-10 -mt-4 md:space-y-0 space-y-6">
                <div v-for="category in  categories " :key="category.id"
                    class="p-4 md:w-1/3 flex flex-col text-center items-center">
                    <div class="flex-grow">
                       <h1>Category-Slug - {{ category.slug }}</h1>
                    </div>
                </div>
            </div>
        </section>
    </div>
</template>





