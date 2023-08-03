<script setup>
/* Navigation will occur before fetching is complete.
  Handle pending and error states directly within your component's template
*/
const route = useRoute()
console.log('route slug is here --> ', route)
const { pending, error, data: posts
} = await useLazyAsyncData('data', () => $fetch(`http://localhost:8000/api/category/${route.params.slug}`));
console.log('Hello', posts)
console.log('pending', pending)
console.log('error', error)

// const route = useRoute()
// console.log('route slug is here --> ', route.params.slug)
// const { data: post_detail
// } = await useLazyAsyncData('post', () => $fetch(`http://localhost:8000/api/${route.params.slug}/`))
// console.log('what is single data is coming ', post)

</script> 

<template>
    <div>
        <section class="text-gray-600 body-font">
            <div class="container px-5 py-24 mx-auto">
                <div v-if="pending" class="text-center mb-20">
                    <h1 class="sm:text-3xl text-2xl font-medium title-font text-gray-900 mb-4">Raw Denim Heirloom Man Braid
                    </h1>
                    <p class="text-base leading-relaxed xl:w-2/4 lg:w-3/4 mx-auto text-gray-500s">Blue bottle crucifix vinyl
                        post-ironic four dollar toast vegan taxidermy. Gastropub indxgo juice poutine, ramps microdosing
                        banh mi pug.</p>
                    <div class="flex mt-6 justify-center">
                        <div class="w-16 h-1 rounded-full bg-indigo-500 inline-flex"></div>
                    </div>
                </div>
                <div v-if="error">
                    {{ error }}
                </div>

                <div class="flex flex-wrap sm:-m-4 -mx-4 -mb-10 -mt-4 md:space-y-0 space-y-6">
                    <div v-for="post in posts" :key="post.id" class="p-4 md:w-1/3 flex flex-col text-center items-center">
                        <PostAll :post="post" />
                    </div>
                </div>
            </div>
        </section>
    </div>
</template>
