<template>
    <div class="flex-grow">
        <h2 class="text-gray-900 text-lg title-font font-medium mb-3">
            <li class="mr-5 list-none hover:text-cyan-600">
                <NuxtLink :to="{
                    name: 'posts-slug',
                    params: { slug: post.slug }
                }">
                    <p>{{ post.title }}</p>
                </NuxtLink>
            </li>
        </h2>
        <h1 class="leading-relaxed text-base">
            Title - {{ post.title }}
        </h1>
        <p>Description - {{ post.description }}</p>
        <br>
        <h1 class="leading-relaxed text-base">
            <li class="mr-5 list-none hover:text-cyan-600">
                <NuxtLink :to="{
                    name: 'category-slug',
                    params: { slug: post.category_name }
                }">
                    <p>{{ post.category_name }}</p>
                </NuxtLink>
            </li>
        </h1>
        <div v-for="image in  post.blog_post_image" class="p-4 md:w-1/3 flex flex-col text-center items-center">
            <nuxt-img :src="image.image" placeholder="Elise is here" loading="lazy" sizes="sm:100vw md:50vw lg:400px" />
            <p>Alter Nativ Text - {{ image.alt_text }}</p>
        </div>
    </div>
</template>

<script setup>
const { post } = defineProps(['post'])

</script>