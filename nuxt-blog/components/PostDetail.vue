<template>
    <div>
        <div class="foxe-200">
            <div class="container">
                <div class="left-column">
                    <h3>{{ post.id }}</h3>
                    <h3>{{ post.title }}</h3>
                </div>
            </div>
        </div>
    </div>
</template>

<script setup>
const { post } = defineProps(['post'])
</script>
