<script setup>
const route = useRoute()
console.log('i am route--> ', route)
const { pending, error, data: post
} = await useLazyAsyncData('post', () => $fetch(`http://localhost:8000/api/${route.params.slug}/`))
console.log('what is single data is coming ', post)

</script>

<template>
    <div class="foxe-200">
        <h1>Detil Page</h1>
        <h1 v-if="error">Oops! Error encountered: {{ error }}</h1>
        <h1 v-if="pending">Pending ... </h1>
        <div v-if="post">
            <PostDetail :post="post" />
            <!-- <div class="container">
                <div class="left-column">
                    <h3>{{ post.id }}</h3>
                    <h3>{{ post.title }}</h3>
                </div>
            </div> -->
        </div>
        <div class="grid grid-flow-row">
            <div class="columns-md">
                <button class="btn btn-primary">GoAhead</button>
            </div>
            <div class="columns-md">
                <button class="btn btn-primary">GoBack</button>
            </div>
        </div>
    </div>
</template>