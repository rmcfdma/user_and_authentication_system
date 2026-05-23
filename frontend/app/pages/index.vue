<script setup lang="ts">
import * as z from "zod";
import type { FormSubmitEvent, AuthFormField } from "@nuxt/ui";
import GoogleSvg from "~/assets/svg/google.svg";
import FacebookSvg from "~/assets/svg/facebook.svg";

const toast = useToast();

const fields: AuthFormField[] = [
  {
    name: "email",
    type: "email",
    label: "Email",
    placeholder: "Coloque seu email",
    required: true,
  },
  {
    name: "password",
    label: "Senha",
    type: "password",
    placeholder: "Coloque sua senha",
    required: true,
  },
  {
    name: "remember",
    label: "Remember me",
    type: "checkbox",
  },
];

const providers = [
  {
    label: "Google",
    icon: "i-simple-icons-google",
    onClick: () => {
      toast.add({ title: "Google", description: "Login com Google" });
    },
  },
  {
    label: "GitHub",
    icon: "i-simple-icons-github",
    onClick: () => {
      toast.add({ title: "GitHub", description: "Login com GitHub" });
    },
  },
];

const schema = z.object({
  email: z.email("Email inválido"),
  password: z.string("Senha obrigatória.").min(8, "Mínimo de 8 caracteres"),
});

type Schema = z.output<typeof schema>;

const onSubmit = (payload: FormSubmitEvent<Schema>) => {
  console.log("Submitted", payload);
}
</script>

<template>
  <div class="flex flex-col items-center justify-center gap-4 p-4">
    <UPageCard class="w-full max-w-md">
      <UAuthForm
        :schema="schema"
        title="Login"
        description="Entre com sua credenciais."
        icon="i-lucide-user"
        :fields="fields"
        :submit="{
            label: 'Entrar'
  }"
        @submit="onSubmit"
      />

      <div class="mt-3 space-y-5">
        <USeparator label="Ou continue com" />

        <UButton block color="neutral" variant="outline">
          <template #leading>
            <img :src="GoogleSvg" class="size-5" alt="Google" />
          </template>

          Google
        </UButton>

        <UButton block color="neutral" variant="outline">
          <template #leading>
            <img :src="FacebookSvg" class="size-5" alt="Google" />
          </template>
          Facebook
        </UButton>
      </div>
    </UPageCard>
  </div>
</template>
